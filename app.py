import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from database import init_db
from seed_data import seed
from routes.pets import pets_bp
from routes.adopt import adopt_bp
from routes.contact import contact_bp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend'))

app = Flask(__name__)
CORS(app)

# Register API blueprints
app.register_blueprint(pets_bp)
app.register_blueprint(adopt_bp)
app.register_blueprint(contact_bp)


# ─── Serve Frontend Pages ────────────────────────────────────────────────────

@app.route('/')
def home():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/pets')
def pets():
    return send_from_directory(FRONTEND_DIR, 'pets.html')

@app.route('/adopt')
def adopt():
    return send_from_directory(FRONTEND_DIR, 'adopt.html')

@app.route('/about')
def about():
    return send_from_directory(FRONTEND_DIR, 'about.html')

@app.route('/contact')
def contact():
    return send_from_directory(FRONTEND_DIR, 'contact.html')

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, 'css'), filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, 'js'), filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, 'images'), filename)

@app.route('/<path:filename>')
def serve_static(filename):
    # Handle .html extensions (e.g. /pets.html → pets.html)
    try:
        return send_from_directory(FRONTEND_DIR, filename)
    except Exception:
        return jsonify({'error': 'Page not found'}), 404


# ─── Health check ───────────────────────────────────────────────────────────

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'message': 'Paws & Hearts API is running'})


# ─── Start ───────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    seed()
    print('\n=========================================')
    print('   Paws & Hearts is live!')
    print('   Open your browser: http://localhost:5000')
    print('   Frontend directory: ' + FRONTEND_DIR)
    print('=========================================\n')
    app.run(debug=True, port=5000, host='0.0.0.0')
