from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter()


@router.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    """Accept an image upload and return a disease prediction (placeholder)."""
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Empty file")

    # TODO: load TensorFlow model and run inference on the image
    return {
        "filename": file.filename,
        "prediction": "healthy",
        "confidence": 0.0,
        "message": "Model inference not yet configured",
    }
