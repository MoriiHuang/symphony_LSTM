import json
import os
from music21 import converter,instrument,note,chord,stream
class mid_note_switcher:
    def __init__(self):
        self.song_path=''
        self.name=[]
        self.output_note=[]
    def get_mid_name(self,path):
        self.song_path=path
        for root,dirs,files in os.walk(self.song_path):
            self.name=files
        return self.name 
    def get_notes(self):
        all_notes=[]
        for song_name in self.name[600:]:
            try:
                print(self.song_path+song_name+'\n')
                stream=converter.parse(self.song_path+song_name)
                instru=instrument.partitionByInstrument(stream)
                if instru:
                    notes=instru.parts[0].recurse()
                else:
                    notes=stream.flat.notes
                for element in notes:
                    if isinstance(element,note.Note):
                        all_notes.append(str(element.pitch))
                    elif isinstance(element,chord.Chord):
                        all_notes.append('.'.join(str(n) for n in element.normalOrder))
                print(self.song_path+song_name+'finished')
            except:
                pass
        return all_notes
    def create_music(self,result_data,filename):
        result_data = [str(data) for data in result_data]
        offset = 0
        # 生成 Note（音符）或 Chord（和弦）对象
        for data in result_data:
            if ('.' in data) or data.isdigit():
                notes_in_chord = data.split('.')
                notes = []
                for current_note in notes_in_chord:
                    new_note = note.Note(int(current_note))
                    new_note.storedInstrument = instrument.Piano()
                    notes.append(new_note)
                new_chord = chord.Chord(notes)
                new_chord.offset = offset
                self.output_notes.append(new_chord)

            else:
                new_note = note.Note(data)
                new_note.offset = offset
                new_note.storedInstrument = instrument.Piano()
                self.output_notes.append(new_note)
            offset += 1
        # 创建音乐流（Stream）
        midi_stream = stream.Stream(self.output_notes)
        # 写入 MIDI 文件
        midi_stream.write('midi', fp=filename+'.mid')
sw=mid_note_switcher()
sw.get_mid_name('/Users/lucifer/Desktop/LSTM/data/')
g=sw.name
s=sw.get_notes()
with open ('origin.json','a') as f:
    json.dump(s,f)
    f.write('\n')