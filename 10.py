import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
from matplotlib.widgets import Slider
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Task 1:
plt.figure(figsize=(10, 6))
ax = plt.gca()
ax.set_title('Полиномы Лежандра', fontsize=14, fontweight='bold')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('P(x)', fontsize=12)

x = np.linspace(-1, 1, 500)
colors = plt.cm.jet(np.linspace(0, 1, 7))

for n in range(1, 8):
    P = legendre(n)
    y = P(x)
    ax.plot(x, y, lw=2, color=colors[n-1], label=f'n = {n}')
    if n == 1: ax.annotate(f'n={n}', xy=(0.8, y[400]), xytext=(0.8, 0.7), arrowprops=dict(arrowstyle="->", color=colors[n-1]))
    elif n == 2: ax.annotate(f'n={n}', xy=(0.5, y[250]), xytext=(0.5, 0.5), arrowprops=dict(arrowstyle="->", color=colors[n-1]))
    elif n == 3: ax.annotate(f'n={n}', xy=(0.1, y[50]), xytext=(-0.3, -0.5), arrowprops=dict(arrowstyle="->", color=colors[n-1]))
    elif n == 4: ax.annotate(f'n={n}', xy=(-0.2, y[200]), xytext=(-0.8, 0.5), arrowprops=dict(arrowstyle="->", color=colors[n-1]))
    elif n == 5: ax.annotate(f'n={n}', xy=(-0.5, y[125]), xytext=(-0.8, -0.5), arrowprops=dict(arrowstyle="->", color=colors[n-1]))
    elif n == 6: ax.annotate(f'n={n}', xy=(0.6, y[300]), xytext=(0.6, 0.7), arrowprops=dict(arrowstyle="->", color=colors[n-1]))
    else: ax.annotate(f'n={n}', xy=(0, y[250]), xytext=(0, 0.5), arrowprops=dict(arrowstyle="->", color=colors[n-1]))

ax.legend(loc='best')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Task 2:
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Фигуры Лисажу', fontsize=16, fontweight='bold')
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]
t = np.linspace(0, 2 * np.pi, 1000)

for i, (a, b) in enumerate(ratios):
    row, col = i // 2, i % 2
    ax = axs[row, col]
    x = np.sin(a * t)
    y = np.sin(b * t)
    ax.plot(x, y, lw=2, color='purple')
    ax.set_title(f'Соотношение частот: {a}:{b}', fontsize=12)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Task 3: 
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.set_title('Анимация фигуры Лисажу', fontsize=14, fontweight='bold')
ax3.set_xlim(-1.5, 1.5)
ax3.set_ylim(-1.5, 1.5)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.set_aspect('equal')

t = np.linspace(0, 2 * np.pi, 1000)
line, = ax3.plot([], [], lw=2, color='green')
ratio_text = ax3.text(0.05, 0.95, '', transform=ax3.transAxes, fontsize=12)

def init():
    line.set_data([], [])
    ratio_text.set_text('Соотношение: 0:0')
    return line, ratio_text

def animate(i):
    ratio = i / 100
    x = np.sin(ratio * t)
    y = np.sin(1 * t)
    line.set_data(x, y)
    ratio_text.set_text(f'Соотношение: {ratio:.2f}:1')
    return line, ratio_text

ani = animation.FuncAnimation(fig3, animate, init_func=init, frames=100, interval=100, blit=True)

# Task 4: 
fig4 = plt.figure(figsize=(14, 10))
fig4.suptitle('Сложение двух волн', fontsize=16, fontweight='bold')

ax_wave1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax_wave2 = plt.subplot2grid((3, 3), (1, 0), colspan=3)
ax_result = plt.subplot2grid((3, 3), (2, 0), colspan=3)

for ax in [ax_wave1, ax_wave2, ax_result]:
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True, linestyle='--', alpha=0.7)

ax_wave1.set_title('Волна 1: sin(x)')
ax_wave2.set_title('Волна 2: sin(x)')
ax_result.set_title('Результат сложения')

ax_amp1 = plt.axes([0.25, 0.05, 0.65, 0.02])
ax_freq1 = plt.axes([0.25, 0.08, 0.65, 0.02])
ax_amp2 = plt.axes([0.25, 0.11, 0.65, 0.02])
ax_freq2 = plt.axes([0.25, 0.14, 0.65, 0.02])

slider_amp1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=1.0)
slider_freq1 = Slider(ax_freq1, 'Частота 1', 0.5, 3.0, valinit=1.0)
slider_amp2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=1.0)
slider_freq2 = Slider(ax_freq2, 'Частота 2', 0.5, 3.0, valinit=1.0)

x = np.linspace(0, 4*np.pi, 1000)
line1, = ax_wave1.plot(x, np.sin(x), 'r-', lw=2)
line2, = ax_wave2.plot(x, np.sin(x), 'b-', lw=2)
line_res, = ax_result.plot(x, 2*np.sin(x), 'g-', lw=2)

def update(val):
    amp1 = slider_amp1.val
    freq1 = slider_freq1.val
    amp2 = slider_amp2.val
    freq2 = slider_freq2.val
    
    wave1 = amp1 * np.sin(freq1 * x)
    wave2 = amp2 * np.sin(freq2 * x)
    result = wave1 + wave2
    
    line1.set_ydata(wave1)
    line2.set_ydata(wave2)
    line_res.set_ydata(result)
    
    ax_wave1.set_title(f'Волна 1: {amp1:.1f}*sin({freq1:.1f}*x)')
    ax_wave2.set_title(f'Волна 2: {amp2:.1f}*sin({freq2:.1f}*x)')
    fig4.canvas.draw_idle()

slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

plt.tight_layout(rect=[0, 0.15, 1, 0.95])

# Task 5: 
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig5 = plt.figure(figsize=(14, 6))
fig5.suptitle('Функция среднеквадратичного отклонения (MSE)', fontsize=16, fontweight='bold')

ax1 = fig5.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax1.set_title('Линейный масштаб')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')
fig5.colorbar(surf1, ax=ax1, shrink=0.5)

ax2 = fig5.add_subplot(122, projection='3d')
Z_log = np.log(Z + 1e-10)
surf2 = ax2.plot_surface(X, Y, Z_log, cmap='plasma', alpha=0.8)
ax2.set_title('Логарифмический масштаб по оси Z')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(MSE)')
fig5.colorbar(surf2, ax=ax2, shrink=0.5)

ax1.view_init(elev=30, azim=45)
ax2.view_init(elev=30, azim=45)

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()