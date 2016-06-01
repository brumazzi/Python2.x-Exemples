#!/usr/bin/env python
# -*- coding:utf-8 -*-

import struct as st;

package = st.pack("if6s",5,6.023583,"string"); #guarda inteiro, float e 6 caracteres

result = st.unpack("if6s",package);

print result;
