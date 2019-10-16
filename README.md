# RoboGym

A Virtual Training Gym for Autonomous Vehicle using Deep Reinforcement Learning 

# Requirement

The RoboGym package works on Linux, Mac and Windows, as well as most Cloud providers. Note that for submission to the competition we only support linux-based Docker files.  
<!--, for cloud engines check out [this cloud documentation](documentation/cloud.md).-->

We recommend using a virtual environment specifically for the competition. You will need `python3.6` installed (we currently only support **python3.6**). Clone this repository to run the examples we provide.

We offer two packages for this competition:

- The main package is an API for interfacing with the Unity environment.
[ml-agents environments](https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents-envs). you can install it from the source, head to `Packages/` folder and run 
    ```
    pip install -e .
    ```

    In case you wish to create a conda environment you can do so by running: 
    ```
    conda create -n RoboGym python=3.6
    ```

- We also provide a package that can be used as a starting point for training, and which is required to run the baseline model.
[ml-agents' training environment](https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents) that relies on 
[OpenAI's PPO](https://openai.com/blog/openai-baselines-ppo/). 
you can install it from source, head to `examples/animalai_train` and run:
    ```
    pip install -e .
    ```

Finally download the environment for your system:

| OS | Environment link |
| --- | --- |
| Linux |  [download v1.0.0](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_linux_v1.0.0.zip) |
| MacOS |  [download v1.0.0](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_mac_v1.0.0.zip) |
| Windows | [download v1.0.0](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_windows_v1.0.0.zip)  |

You can now unzip the content of the archive to the `env` folder and you're ready to go! Make sure the executable 
`RoboGym.*` is in `env/`. On linux you may have to make the file executable by running `chmod +x env/RoboGym.x86_64`. 


