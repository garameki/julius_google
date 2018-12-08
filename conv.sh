#!/bin/bash

STEM=google

iconv -f utf8 -t eucjp $STEM.txt | yomi2voca.pl | iconv -f eucjp -t utf8 >> $STEM.voca
