FROM hoverbear/archlinux
ADD REQUIREMENTS /
RUN pacman -Syu --noconfirm --force
RUN pacman -S --noconfirm --force python python-pip vim
RUN pip install -r REQUIREMENTS
VOLUME ["/source"]
WORKDIR /source

