import os
import magenta
from magenta.models.melody_rnn import melody_rnn_generate
from magenta.models.shared import sequence_generator_bundle
from magenta.protobuf import generator_pb2
import note_seq

def generate_music(mood):
    # Load the pre-trained Melody RNN model
    model_name = 'basic_rnn'
    bundle_file = f'magenta/models/melody_rnn/bundles/{model_name}.mag'  # Ensure this file exists

    # Initialize the MelodyRnnGenerator with the bundle
    bundle = sequence_generator_bundle.read_bundle_file(bundle_file)
    generator = melody_rnn_generate.MelodyRnnGenerator(bundle)

    # Prepare generator options
    generator_options = generator_pb2.GeneratorOptions()
    generator_options.args['temperature'].float_value = 1.0  # Adjust for creativity
    generator_options.generate_sections.add(start_time=0, end_time=30)  # 30 seconds of music

    # Create an empty NoteSequence (initial condition)
    input_sequence = note_seq.NoteSequence()

    # Generate a melody based on mood
    sequence = generator.generate(input_sequence, generator_options)

    # Save the generated music as a MIDI file
    midi_file = 'generated_melody.mid'
    note_seq.sequence_proto_to_midi_file(sequence, midi_file)

    # Convert MIDI to audio using FluidSynth
    audio_file = 'generated_melody.wav'
    soundfont = 'soundfont.sf2'  # Ensure you have this file
    if not os.path.exists(soundfont):
        raise FileNotFoundError(f'SoundFont file {soundfont} not found.')
    
    os.system(f'fluidsynth -ni {soundfont} {midi_file} -F {audio_file} -r 44100')

    return audio_file
