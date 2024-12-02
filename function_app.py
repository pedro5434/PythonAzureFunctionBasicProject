import logging
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="mytimer")
@app.timer_trigger(schedule="0 */1 * * * *", 
              arg_name="mytimer",
              run_on_startup=True) 
def timer_trigger(mytimer: func.TimerRequest) -> None:
    logging.info('>> START <<')
    logging.info('>> END <<')
