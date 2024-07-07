// imports
use std::fs;
use std::fs::File;
use std::io::Read;
use std::io::Write;
use std::path::{PathBuf};
use sha2::{Digest, Sha256};
use sysinfo::Disks;

// compare sha-2 against two files
#[tauri::command]
pub fn hash_check(file_path1: String, file_path2: String) -> Result<bool, String> {
    // read first file
    let mut file1 = File::open(file_path1).map_err(|e| format!("Failed to open file 1: {}", e))?;
    let mut contents1 = Vec::new();
    file1.read_to_end(&mut contents1).map_err(|e| format!("Failed to read file 1: {}", e))?;
    // read second file
    let mut file2 = File::open(file_path2).map_err(|e| format!("Failed to open file 2: {}", e))?;
    let mut contents2 = Vec::new();
    file2.read_to_end(&mut contents2).map_err(|e| format!("Failed to read file 2: {}", e))?;
    // calculate sha-2 hashes
    let hash1 = Sha256::digest(&contents1);
    let hash2 = Sha256::digest(&contents2);
    // compare the hashes
    Ok(hash1 == hash2)
}

// write text to a file at a path
#[tauri::command]
pub fn write_text(path: String, text: String) -> Result<(), String> {
    // create the file
    let mut file = match File::create(&path) {
        Ok(file) => file,
        Err(e) => return Err(format!("Failed to create file: {}", e)),
    };
    // write the contents to the file
    if let Err(e) = file.write_all(text.as_bytes()) {
        return Err(format!("Failed to write to file: {}", e));
    }
    // success (?)
    Ok(())
}

// copy a file to another destination
#[tauri::command]
pub fn copy_file(from: String, to: String) -> Result<(), String> {
    // read the file
    let mut file = File::open(&from).map_err(|e| format!("Failed to open file: {}", e))?;
    let mut contents = Vec::new();
    file.read_to_end(&mut contents).map_err(|e| format!("Failed to read file: {}", e))?;
    // write the file
    let mut file = File::create(&to).map_err(|e| format!("Failed to create file: {}", e))?;
    file.write_all(&contents).map_err(|e| format!("Failed to write file: {}", e))?;
    // success (?)
    Ok(())
}

// move a file
#[tauri::command]
pub fn move_file(from: String, to: String) -> Result<(), String> {
    // copy the file
    copy_file(from.clone(), to.clone())?;
    // delete the original
    if let Err(e) = std::fs::remove_file(from) {
        return Err(format!("Failed to delete file: {}", e));
    }
    // success (?)
    Ok(())
}

// create a folder
#[tauri::command]
pub fn create_path(path: String) -> Result<(), String> {
    let path_buf = PathBuf::from(path);
    if let Err(e) = fs::create_dir_all(&path_buf) {
        return Err(format!("Failed to create folder: {}", e));
    }
    Ok(())
}

// see if enough disk space exists
#[tauri::command]
pub fn enough_space(path: &str, required_space: u64) -> bool {
    let disks = Disks::new_with_refreshed_list();
    for disk in disks.list() {
        if let Some(mount_point) = disk.mount_point().to_str() {
            if path.starts_with(mount_point) {
                if disk.available_space() >= required_space {
                    return true;
                } 
            }
        }
    }
    false
}