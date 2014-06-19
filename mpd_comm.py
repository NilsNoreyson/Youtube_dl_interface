__author__ = 'peterb'

import serial
import datetime
from mpd import MPDClient
from flask import Flask,jsonify


def get_playlists_from_mpd():
    client=MPDClient()
    mopidyAddress = '192.168.13.13'
    mopidyPort = 6600

    client.timeout = 10
    client.idletimeout = None
    client.connect(mopidyAddress,mopidyPort)
    client.password('IlPits2013')
    playlists=client.listplaylists()
    client.disconnect()
    return playlists

def load_playlist(name):
    client=MPDClient()
    mopidyAddress = '192.168.13.13'
    mopidyPort = 6600

    client.timeout = 10
    client.idletimeout = None
    client.connect(mopidyAddress,mopidyPort)
    client.password('IlPits2013')
    client.clear()
    client.load(name)
    client.disconnect()
    return


if __name__=='__main__':

    playlists=get_playlists_from_mpd()
    print playlists
    just_namelist=[p['playlist'] for p in playlists]
    print(just_namelist)
    load_playlist(just_namelist[7])
    # tracks=client.listplaylistinfo('schlafantonschlaf')
    #
    # for t in tracks:
    #     print t['title']


