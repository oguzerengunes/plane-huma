// Hüma ince kabuk: Plane URL'yi sarmalar, bildirim+updater sağlar
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_notification::init())
        .plugin(tauri_plugin_updater::Builder::new().build())
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_process::init())
        .setup(|app| {
            let _w = app.get_webview_window("main").unwrap();
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("Tauri çalıştırma hatası");
}
