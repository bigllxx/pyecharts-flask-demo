import json
from random import randrange

from starlette.templating import Jinja2Templates
from fastapi import FastAPI, Request

from pyecharts import options as opts
from pyecharts.charts import Bar

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.get("/barChart")
async def get_bar_chart():
    c = bar_base()
    return json.loads(c.dump_options_with_quotes())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="127.0.0.1", port=5001, reload=True)
