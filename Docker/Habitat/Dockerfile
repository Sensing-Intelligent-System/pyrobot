FROM argsis/locobot:NUC

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO melodic

############################# Habitat install ##################################
RUN sudo apt-get install -y --no-install-recommends python3-pip

RUN pip3 install --upgrade pip setuptools

RUN pwd && git clone --branch stable https://github.com/facebookresearch/habitat-sim.git

RUN sudo apt-get install -y libjpeg-dev libopenblas-dev libglm-dev libgl1-mesa-glx libegl1-mesa-dev mesa-utils xorg-dev freeglut3-dev

# RUN sudo make install
RUN sudo apt-get install -y libopenblas-dev
RUN sudo apt install libomp-dev
RUN sudo apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libzmqpp-dev \
    libopencv-dev 

#RUN cd ${HOME}/habitat-sim/ && pwd && sudo python3 setup.py install # Inside PyRobot Virtual Environment
RUN cd ${HOME}/habitat-sim/ && pwd && sudo python3 setup.py build_ext --parallel 1 install
RUN pip3 install -e


# RUN . ${HOME}/pyenv_pyrobot_python3/bin/activate
# RUN cd ${HOME}/habitat-sim/ && pwd && pip3 install -r requirements.txt # Inside PyRobot Virtual Environment

# #RUN echo "apt install" 
# RUN sudo apt-get install -y libomp-dev libjpeg-dev libopenblas-dev libglm-dev libgl1-mesa-glx libegl1-mesa-dev mesa-utils xorg-dev freeglut3-dev
# RUN sudo apt-get install -y libopenblas-dev
# RUN sudo apt install libomp-dev


#RUN echo "setup.py"


# python setup.py install --with-cuda for cuda enabled machines.
                                                                            
