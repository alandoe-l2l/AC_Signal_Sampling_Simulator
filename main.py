import numpy as np
import matplotlib.pyplot as plt

actual_freq = 60 #Hz        This is the actual frequency returned by the current transformer.
sample_interval = 6  #msec  This is the sample interval of the SensorBot.
elapsed_time = 1 #sec       This is the elapsed time to show on the chart.
samples = 50    #           This places a marker on the chart after the number of samples have been captured.

plt.figure(figsize=(12, 4))
#create actual signal
plt.plot(t2 := np.linspace(0, elapsed_time, 10000), np.sin(2 * np.pi * actual_freq * t2), 'b', label=f"Continuous Signal ({actual_freq}Hz)")

#create signal sampled
t = np.linspace(0, elapsed_time, int(elapsed_time/(sample_interval/1000)), endpoint=False)
end = (t[samples])
plt.plot(t, np.sin(2 * np.pi * actual_freq * t), 'r', label='Discrete Samples (interpolated)')
plt.plot(end, np.sin(2 * np.pi * actual_freq * end), 'k*', label=f'Sample #{samples}', markersize=10)

#arrange and annotate plot
plt.xlabel('Seconds Elapsed')
plt.ylabel('Voltage Measured')
plt.title('Sampled Voltage vs. Actual Signal')
plt.subplots_adjust(bottom=0.2)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=10)

plt.show()
