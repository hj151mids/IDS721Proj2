from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello! Welcome to the prime number identifier"}

@app.get("/is_prime/{num}")
def is_prime(num:int):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return {"Prime Number": flag}
    else:
        return {"Prime Number": flag}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')