from pydantic_settings import BaseSettings
from pydantic import BaseModel
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from pathlib import Path
from typing import ClassVar
from fastapi.templating import Jinja2Templates

class Settings(BaseSettings):
    DB_URL: str = 'sqlite+aiosqlite:///./teste.db/'
    DBBaseModel: DeclarativeMeta = declarative_base()
    TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(directory='templates')
    MEDIA: ClassVar[Path] = Path('media')
    

    class config:
        case_sensitive = True

settings: Settings = Settings()
