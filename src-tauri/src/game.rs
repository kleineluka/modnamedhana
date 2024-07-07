// crates
extern crate fs_extra;

// imports
use tauri::Window;
use std::path::Path;
use fs_extra::dir::CopyOptions;
use fs_extra::dir::copy;

// modules
use crate::utils;

// store how much disk space we need
const REQUIRED_SPACE: u64 = (1.5 * 1024.0 * 1024.0 * 1024.0) as u64; // 1.5 GB
const GAME_FOLDER: &str = "Repurpose-Hana-Mod";

// store the file path for later
static mut FILE_PATH: Option<String> = None;

// make sure that the path selected IS the game path
#[tauri::command]
pub fn verify_path(file_path: &str) -> bool {
    // store the file path (bleh.. unsafe)
    unsafe {
        FILE_PATH = Some(file_path.to_string());
    }
    // establish file path and required files
    let path = Path::new(file_path);
    let required_items = [
        ("Repurpose.py", false), // (name, is_dir)
        ("lib", true),
        ("renpy", true),
        ("game", true),
    ];
    // see if they all exist
    required_items.iter().all(|(item, is_dir)| {
        let item_path = path.join(item);
        if *is_dir {
            item_path.is_dir()
        } else {
            item_path.exists()
        }
    })
}

// install the mod
#[tauri::command]
pub fn install_mod(window: Window, install_type: String) {
    // get the path
    let path = unsafe { FILE_PATH.clone() }.unwrap_or("No game folder specified".to_string());
    // get a path one level up from it
    let parent_path = Path::new(&path).parent().unwrap();
    print!("Parent path: {:?}", parent_path);
    // step one: verify there is enough space on the disk
    let _ = window.emit("log-update", "Verifying there is enough space on disk...") ;
    if !utils::enough_space(parent_path.to_str().unwrap(), REQUIRED_SPACE) {
        let _ = window.emit("log-update", "Not enough space available.");
        let _ = window.emit("update-error", "no-space");
        return;
    }
    let _ = window.emit("log-update", "Enough space is available!");
    // branch based on install type, if else "copy" or "patch"
    match install_type.as_str() {
        "copy" => {
            // step two: create a new path for the game
            let _ = window.emit("log-update", "Creating a new path for the game...");
            let new_path = parent_path.join(GAME_FOLDER);
            if new_path.exists() {
                let _ = window.emit("update-error", "already-exists");
                return;
            }
            match utils::create_path(new_path.to_str().unwrap().to_string()) {
                Ok(_) => {
                    let _ = window.emit("log-update", "Successfully created directory...");
                }
                Err(_e) => {
                    let _ = window.emit("update-error", "create-dir");
                    return;
                }
            }
            // step three: copy the game files to the new path
            let _ = window.emit("log-update", "Copying game files to new path...");
            let options = CopyOptions::new().content_only(true);
            match copy(path, new_path, &options) {
                Ok(_) => {
                    let _ = window.emit("log-update", "Successfully copied game files...");
                }
                Err(_e) => {
                    let _ = window.emit("update-error", "copy-files");
                    return;
                }
            }
        }
        "patch" => {
            println!("Patching files in game folder...");
        }
        _ => {
            // do nothing
        }
    }
}