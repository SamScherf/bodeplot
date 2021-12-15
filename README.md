# bodeplot
Python module for creating bode plots from arrays of complex numbers

## Usage

Simply import bodeplot and create a bode object by passing it frequency bounds:

```python
import bodeplot

bode = bodeplot([1e-2, 1e2])
```

You can now call the plot method to plot your various frequency responses:

```python
bode.plot(freq, fr, label="My label")
```

And save your plot with the save method:

```python
bode.save("myPlot.png")
```

When initializing the bode class, you can optionally set dB=True or rads=True to have the magnitude/phase be
displayed in decibels or radians respectively.
