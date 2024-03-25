
from fastapi import APIRouter, Response
from matplotlib import pyplot as plt
import io

router: APIRouter = APIRouter()


@router.get("/graph-image")
async def generate_graph_image():
    # Generar la imagen con Matplotlib
    plt.plot([1, 2, 3, 4])
    plt.ylabel('Algunos números')
    plt.xlabel('Otros números')
    # Convertir la imagen a bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    # Servir la imagen
    return Response(content=buffer.getvalue(), media_type="image/png")
