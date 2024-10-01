First attempt at running a AI model locally

* installed python
  * `brew install python3`
* I couldn't find pip so I `sudo ln -s /usr/local/bin/pip3 /usr/local/bin/pip`
* I had to create a python venv `python3 -m venv venv`
* I had to activate the venv `source venv/bin/activate`
* I had to change the pycharm interpreter to the venv
* followed the [steps](https://huggingface.co/allenai/Molmo-7B-D-0924) from the molmo model on huggingface
* Got some error the first time I ran it and needed to install another python dependencie `pip install 'accelerate>=0.26.0'`
* Numpy issue ran - `pip install "numpy<2"`
* 