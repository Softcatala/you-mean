#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2017 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import hunspell
import os.path
import sys


def load_dicts():
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    spellchecker = hunspell.HunSpell(os.path.join(location, "hunspell", "es_ANY.dic"), os.path.join(location, "hunspell", "es_ANY.aff"))
    return spellchecker
    

def means(text):
    print("text: {0}".format(text))
    spellchecker = load_dicts()
    enc = spellchecker.get_dic_encoding()

    for word in text.split(' '):
        if spellchecker.spell(word) is False:
            results = spellchecker.suggest(word)
            correction = ''
            cnt = len(results)
            for i in range(cnt):
                if i == 0:
                    correction = "{0} -> {1} ".format(word, results[0].decode(enc))
                    continue

                correction += "({0})".format(results[i].decode(enc))
                if i + 1 < cnt:
                    correction += ", "
           
            print (correction)
           

def main(argv):
    means(argv[0])

if __name__ == "__main__":
    print ("Usage you-mean 'a sentence'. Default language Spanish")
    print ("Sample: you-mean 'condusco un camion'")
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    
    
#if __name__ == '__main__':
#    app.debug = True
#    app.run()
