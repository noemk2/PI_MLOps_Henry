from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "ier"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# ("/duration?year=123&platform=botella&duration_type=12")
@app.get("/duration/")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    peliculas = []
    if year:
        peliculas = [p for p in peliculas if nombre.lower()
                     in p["nombre"].lower()]
    if platform:
        peliculas = [p for p in peliculas if p["anio"] == anio]

    if duration_type:
        peliculas = [p for p in peliculas if genero.lower()
                     in p["genero"].lower()]
    return peliculas

    # return {"year": year, "platform": platform, "duration_type": duration_type}
