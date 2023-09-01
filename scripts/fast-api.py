from fastapi import FastAPI

app = FastAPI()

# Contador de solicitações
request_count = 0

@app.get('/fastapi')
def read_root():
    return {"message": "Hello from FastAPI!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
