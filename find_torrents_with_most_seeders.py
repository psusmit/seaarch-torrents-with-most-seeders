from tpblite import TPB
from tpblite import CATEGORIES, ORDERS
t = TPB()
torrents = t.search('public domain')

torrents = t.top(category=CATEGORIES.PORN.ALL, last_48=True)
torrent = torrents.getBestTorrent(min_seeds=100, min_filesize='1 MiB', max_filesize='500 GiB')
print('title: ',torrent.title,' is_trusted: ',torrent.is_trusted,' link: \n',torrent.magnetlink)


torrents1 = t.top(category=CATEGORIES.AUDIO.ALL, last_48=True)
torrent = torrents1.getBestTorrent(min_seeds=100, min_filesize='1 MiB', max_filesize='500 GiB')
print('title: ',torrent.title,' is_trusted: ',torrent.is_trusted,' link: \n',torrent.magnetlink)

torrents2 = t.top(category=CATEGORIES.VIDEO.ALL, last_48=True)
torrent = torrents2.getBestTorrent(min_seeds=100, min_filesize='1 MiB', max_filesize='500 GiB')
print('title: ',torrent.title,' is_trusted: ',torrent.is_trusted,' link: \n',torrent.magnetlink)

##torrents3 = t.top(category=CATEGORIES.APPLICATIONS.ALL, last_48=True)
##torrent = torrents3.getBestTorrent(min_seeds=100, min_filesize='1 MiB', max_filesize='500 GiB')
##print('title: ',torrent.title,' is_trusted: ',torrent.is_trusted,' link: \n',torrent.magnetlink)

torrents4 = t.top(category=CATEGORIES.GAMES.ALL, last_48=False)
torrent = torrents4.getBestTorrent(min_seeds=100, min_filesize='1 MiB', max_filesize='500 GiB')
print('title: ',torrent.title,' is_trusted: ',torrent.is_trusted,' link: \n',torrent.magnetlink)

torrents5 = t.top(category=CATEGORIES.ALL, last_48=True)
torrent = torrents5.getBestTorrent(min_seeds=100, min_filesize='1 MiB', max_filesize='500 GiB')
print('title: ',torrent.title,' is_trusted: ',torrent.is_trusted,' link: \n',torrent.magnetlink)

##torrents5 = t.top(category=CATEGORIES.OTHER, last_48=True)
##torrent = torrents5.getBestTorrent(min_seeds=100, min_filesize='1 MiB', max_filesize='500 GiB')
##print('title: ',torrent.title,' is_trusted: ',torrent.is_trusted,' link: \n',torrent.magnetlink)








