from tugas1 import app

print(app)
if __name__ == '__main__':
   app.run(port=8099, debug=True, host='0.0.0.0', threaded=True)
