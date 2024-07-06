
// prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

// modules
mod utils;
mod commands; 
mod game;

// main
fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            utils::hash_check,
            utils::write_text,
            utils::copy_file,
            utils::move_file,
            utils::create_path,
            utils::enough_space,
            commands::navigate, 
            commands::folderwalk,
            game::verify_path,
            game::install_mod])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
