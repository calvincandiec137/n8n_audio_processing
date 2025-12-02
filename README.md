

# Audio Processing API

A minimal Flask-based API that processes uploaded audio using FFmpeg.
The API applies pitch and tempo modifications to an input file and returns the transformed output.
Core logic is in the `app.py` file. 

---

## Features

* Accepts audio files via `POST /process-audio`
* Uses FFmpeg backend
* Applies pitch increase (via `asetrate=44100*1.3`)
* Slows tempo to 0.9x
* Returns processed audio as downloadable `.mp3`

---

## Project Structure

```
├── app.py
├── Dockerfile
├── docker-compose.yml
├── package_n8n.sh
```

---

## Requirements

* Python 3.10+
* FFmpeg installed on host
* pip / virtualenv
* Docker (optional but recommended)

---

## Setup (Local Machine)

1. Create a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```
   pip install flask
   ```

3. Ensure FFmpeg is installed:

   ```
   ffmpeg -version
   ```

4. Run the server:

   ```
   python app.py
   ```

The server will start at:

```
http://0.0.0.0:5000
```

---

## Setup (Docker)

1. Build the image:

   ```
   docker build -t audio-api .
   ```

2. Run the container:

   ```
   docker run -p 5000:5000 audio-api
   ```

Or use:

```
docker compose up -d
```

---

## API Usage

### Endpoint

`POST /process-audio`

### Form-Data Parameters

| Key  | Type | Description       |
| ---- | ---- | ----------------- |
| file | File | Audio file upload |

### Example Using `curl`:

```
curl -X POST http://localhost:5000/process-audio \
  -F "file=@your_audio_file.mp3" \
  --output processed.mp3
```

---

## Notes / Limitations

* Only one file per request.
* Output format is always `.mp3`.
* Processing uses temporary files; container platforms should mount a writable filesystem.

---

## License (MIT)

```
MIT License
```