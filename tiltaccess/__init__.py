from tiltaccess.tiltblescan import extract_temp_and_sg

def get_data():
    raw = extract_temp_and_sg()
    return {
            "temp": int(raw[0]),
            "sg": float(raw[1]) / 1000.0 }
