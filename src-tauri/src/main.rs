
// prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

// modules
mod commands; 
mod game;

// main
fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::navigate, 
            commands::folderwalk,
            game::verify_path])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
