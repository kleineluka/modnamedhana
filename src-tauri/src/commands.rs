
// imports
use tauri::Window;
use tauri::api::dialog::FileDialogBuilder;

// navigate to different pages
#[tauri::command]
pub async fn navigate(window: Window, page: String) {
    let _ = window.eval(&format!("window.location.replace('{}')", page));
}

// open a file explorer to pick a directory
#[tauri::command]
pub async fn folderwalk(window: Window) {
    tauri::async_runtime::spawn(async move {
        FileDialogBuilder::new()
            // let user pick a directory
            .pick_folder(move |folder_path| {
                if let Some(path) = folder_path {
                    println!("Selected folder: {}", path.display().to_string());
                    // send back to front-end
                    if let Err(e) = window.emit("selected-folder", path.display().to_string()) {
                        println!("Error emitting event: {:?}", e);
                    } else {
                        println!("Event emitted successfully");
                    }
                } else {
                    println!("No folder selected");
                }
            });
    });
}