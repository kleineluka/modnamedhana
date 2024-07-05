use std::fs::File;
use std::io::Read;
use std::io::Write;
use sha2::{Digest, Sha256};

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
    // create the folder
    if let Err(e) = std::fs::create_dir_all(&path) {
        return Err(format!("Failed to create folder: {}", e));
    }
    // success (?)
    Ok(())
}

// take in a path and a required size, and then return true/false if the path has enough space
#[tauri::command]
pub fn path_space(file_path: &str, required_space: u64) -> bool {
    // get the path
    let path = Path::new(file_path);
    // get the space
    let space = match path.metadata() {
        Ok(meta) => meta.len(),
        Err(_) => 0,
    };
    // return if it has enough space
    space >= required_space
}