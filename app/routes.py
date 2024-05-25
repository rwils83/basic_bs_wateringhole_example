from flask import current_app as app, send_from_directory, render_template, redirect, url_for
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    file_path = os.path.join(app.root_path, 'files')
    response = send_from_directory(file_path, 'example.exe', as_attachment=True)
    response.headers["Content-Disposition"] = "attachment; filename=example.exe"
    return response

@app.route('/redirect_after_download')
def redirect_after_download():
    return render_template('video.html')

@app.route('/broken')
def broken():
    return render_template('broken.html')