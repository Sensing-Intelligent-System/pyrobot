FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04 

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO melodic

###################################### user #####################################

ENV SHELL=/bin/bash \
    USER=sis \
    UID=1000 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV HOME=/home/${USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${UID} \
    ${USER} 

RUN echo "root:root" | chpasswd
RUN echo "${USER}:111111" | chpasswd

Run apt-get update && apt-get install -y \
    curl \
    lsb-release \
    sudo \
    software-properties-common  \
    tzdata

##################################### setting #####################################
RUN chown -R ${USER}:${USER} ${HOME}/
RUN echo "sis ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers

# setup entrypoint
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]

USER ${USER}

WORKDIR ${HOME}

############################# LoCoBot and PyRobot ############################
RUN curl 'https://raw.githubusercontent.com/facebookresearch/pyrobot/master/robots/LoCoBot/install/locobot_install_all.sh' > locobot_install_all.sh && chmod +x locobot_install_all.sh

RUN chmod +x locobot_install_all.sh

RUN ./locobot_install_all.sh -t full -p 3 -l interbotix

RUN rm locobot_install_all.sh

RUN pip install gtsam

############################# Habitat install ##################################
# RUN source ~/pyenv_pyrobot_python3/bin/activate

RUN git clone --branch stable https://github.com/facebookresearch/habitat-sim.git

RUN sudo apt-get install -y --no-install-recommends python3-pip ## me
RUN pip3 install --upgrade pip setuptools ## me

RUN /bin/bash -c "source ${HOME}/pyenv_pyrobot_python3/bin/activate && cd ${HOME}/habitat-sim/ && pip3 install -r requirements.txt"
# . ${HOME}/pyenv_pyrobot_python3/bin/activate &&
RUN sudo apt-get install -y libjpeg-dev \
    libglm-dev \
    libgl1-mesa-glx \
    libegl1-mesa-dev \
    mesa-utils \
    xorg-dev \
    freeglut3-dev

RUN /bin/bash -c "source ${HOME}/pyenv_pyrobot_python3/bin/activate && cd ${HOME}/habitat-sim/ && sudo python3 setup.py build_ext --parallel 3 install"

RUN mv ${HOME}/pyrobot_catkin_ws/src/* ${HOME}/low_cost_ws/src
RUN rm -rf ${HOME}/pyrobot_catkin_ws && rm -r ${HOME}/low_cost_ws/devel ${HOME}/low_cost_ws/build
