from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Return homepage."""
    madlib_prompts = story.prompts
    return render_template("form.html", prompts=madlib_prompts)


@app.route('/story')
def madlib_story():
    "Returns the finished story based on the inputs from the form"

    madlib_prompts = story.prompts
    ans = {}
    for prompt in madlib_prompts:
        ans.update({f"{prompt}": request.args[prompt]})
    final_story = story.generate(ans)
    return render_template("your_story.html", story=final_story)
