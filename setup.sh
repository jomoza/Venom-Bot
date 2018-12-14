wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
tar xvf Python-3.6.3.tgz
cd Python-3.6.3
./configure --enable-optimizations
make -j8
make altinstall
pip3.6 install --upgrade pip
pip3.6 install discord.py
pip3.6 install asyncio
