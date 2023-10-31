import numpy as np
import matplotlib.pyplot as plt
def sound_plot(signal, sample_rate, title):
    sig_np = signal.numpy()
  
    num_channel, num_frames = sig_np.shape

    time_axis = torch.arange(0, num_frames) / sample_rate

    fig, axes = plt.subplots(num_channel, 1)

    if(num_channel == 1): axes = [axes]

    for k in range(num_channel):
        axes[k].plot(time_axis, sig_np[k], lw = 1)
        axes[k].grid(True)
        if(num_channel > 1): axes[k].set_ylabel(f'channel {k+1}')
    
    fig.suptitle(title)
    plt.show(block=False)
    
def sound_spec(spec):
    fig, axis = plt.subplots(1, 1)
    axis.set_xlabel(" time ")
    axis.set_ylabel(" mels ")
    axis.imshow(spec, origin="lower", aspect="auto")
    plt.show(block=False)