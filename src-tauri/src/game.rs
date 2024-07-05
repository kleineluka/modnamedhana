// imports
use std::path::Path;

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