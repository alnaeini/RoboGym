# RoboGym

A Virtual Training Gym for Autonomous Vehicle using Deep Reinforcement Learning 

# Requirement

The RoboGym package works on Linux, Mac and Windows, as well as most Cloud providers(AWS). 

I recommend using a virtual environment and following instruction for training. 

The main package is an API for interfacing with the Unity environment.
[ml-agents environments](https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents-envs). you can install it from the source, head to `Packages/` folder and run 
    ```
    pip install -e .
    ```

    In case you wish to create a conda environment you can do so by running below command in **Packages** folder:
    ```
    conda create -n RoboGym_install.yaml
    ```

[ml-agents' training environment](https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents) that relies on 
[OpenAI's PPO](https://openai.com/blog/openai-baselines-ppo/). 
you can install it from source, head to `examples/RoboGym_train` and run:
    ```
    pip install -e .
    ```

Finally download the baseline environment for your system:

| OS | Environment link |
| --- | --- |
| Linux |  [download v1.0.0](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_linux_v1.0.0.zip) |
| MacOS |  [download v1.0.0](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_mac_v1.0.0.zip) |
| Windows | [download v1.0.0](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_windows_v1.0.0.zip)  |


You can now unzip the content of the archive to the `env` folder and you're ready to go! Make sure the executable 
`RoboGym.*` is in `env/`. On linux you may have to make the file executable by running `chmod +x env/RoboGym.x86_64`. 


