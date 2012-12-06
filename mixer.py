#!/usr/bin/python
import wave

wav1 = wave.open( 'note1.wav', 'r' )
wav2 = wave.open( 'note3.wav', 'r' )
params = wav1.getparams()
print params
rec = wave.open( 'mixing.wav', 'w' )
rec.setparams( ( params[0], params[1], params[2], 88200, params[4], params[5] ) )

seq = ''
for p in range(0, min(88200, wav1.getnframes(), wav2.getnframes()) ): 
    value1 = wave.struct.unpack( "hh", wav1.readframes(1)) 
    value2 = wave.struct.unpack( "hh", wav2.readframes(1)) 
    value = ( ( value1[0] + value2[0] )/2, (value1[1]+value2[1])/2 ) 
    #print value1, value2, value
    seq += wave.struct.pack('h',value[0] )
    seq += wave.struct.pack('h',value[1] )

rec.writeframes( seq ) 
rec.close()

