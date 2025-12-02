from flask import Flask, request, send_file
import subprocess
import os
import tempfile

app = Flask(__name__)

@app.route('/process-audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return {"error": "No file uploaded"}, 400

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return {"error": "Empty filename"}, 400

    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.filename)[1]) as tmp_input:
        uploaded_file.save(tmp_input.name)
        input_path = tmp_input.name

    output_path = input_path.rsplit('.', 1)[0] + "_processed.mp3"

    # Run FFmpeg to change pitch & tempo
    cmd = [
        "ffmpeg",
        "-i", input_path,
        "-filter:a", "asetrate=44100*1.3,atempo=0.9",
        "-y",
        output_path
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": f"FFmpeg failed: {e}"}, 500

    # Return the processed file
    response = send_file(output_path, as_attachment=True)

    # Cleanup temporary input (keep output for sending)
    os.remove(input_path)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
