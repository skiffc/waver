#!/usr/bin/python
import numpy as N
import wave


wav = wave.open( 'scale.wav', 'r' )

#print wav.getnchannels()
#print wav.getsampwidth()
#print type(wav.getsampwidth())
#print wav.getframerate()
#print wav.getnframes()
params = wav.getparams()
print params
interval = 441
waveform = () 
i = 0
zero = 0
begin = True
last = 0
squsum_last = 0
for p in range(0, wav.getnframes()/interval): 
#for p in range(1, 10000): 
    for q in range( 0, interval ):
        value = wav.readframes(1)
        value = wave.struct.unpack( "i", value )[0] 
        if q == 0:
            squsum = value * value / 1000000000000
        else:
            squsum += value * value / 1000000000000
        if not begin:
            waveform += ( value, )
    if squsum > squsum_last:
        pass
        #print p, "L"
    else:
        pass
        #print p, "S"
    squsum_last = squsum
    #print p, value
    #print p, squsum
    if begin:
        waveform = ()
        if squsum < 10000:
            continue
        begin = False
    else:
        if squsum < 10000:
            zero += 1
        if zero > 50:
            begin = True
            zero = 0
            i += 1
            print wav.tell(), wav.tell() - last
            last = wav.tell()
            rec = wave.open( 'note' + str(i) + '.wav', 'w' )
            print ( params[0], params[1], params[2], len(waveform), params[4], params[5] )
            rec.setparams( ( params[0], params[1], params[2], len(waveform), params[4], params[5] ) )
            seq = ''
            for r in range(len(waveform)):
                seq += wave.struct.pack('i',waveform[r] )
            rec.writeframes( seq ) 
            rec.close()

