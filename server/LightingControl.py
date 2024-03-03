import asyncio
import random
import math
from tapo import ApiClient, Color

async def lights_on(lights):
    print("Turning lights on...")
    await asyncio.gather (
        lights[0].on(),
        lights[1].on(),
        lights[2].on(),
        lights[3].on(),
        lights[4].on(),
        lights[5].on()
    )

async def lights_off(lights):
    print("Turning lights off...")
    await asyncio.gather (
        lights[0].off(),
        lights[1].off(),
        lights[2].off(),
        lights[3].off(),
        lights[4].off(),
        lights[5].off()
    )

async def smooth_transition(device, target_hue, target_brightness, duration):
    current_state = await device.get_device_info()

    current_hue = current_state.hue
    current_brightness = current_state.brightness

    # Calculate the step size for hue and brightness
    hue_step = (target_hue - current_hue) / duration
    brightness_step = (target_brightness - current_brightness) / duration

    for _ in range(duration):
        current_hue += hue_step
        current_brightness += brightness_step

        await device.set().brightness(int(current_brightness)).hue_saturation(int(current_hue), 100).send(device)

        # Introduce a slight delay to smooth the transition
        await asyncio.sleep(.1)

async def flicker_candle(device):
    duration = 1000  # Duration of the flicker effect in seconds

    for _ in range(duration):
        flicker_duration = random.uniform(0.1, 0.15)  # Random duration for each flicker
        flicker_intensity = random.randint(20, 24)  # Random intensity of each flicker
        flicker_color = random.randint(34, 40)
        
        await device.set().brightness(flicker_intensity).hue_saturation(flicker_color, 100).send(device)

        # Introduce a random delay for each flicker
        await asyncio.sleep(flicker_duration)

async def ocean_effect(device):
    duration = 60  # Duration of the ocean effect in seconds

    for _ in range(duration):
        target_hue = random.randint(190, 240)  # Random hue in the blue-green range
        target_brightness = random.randint(50, 100)  # Random brightness for shimmering effect

        await smooth_transition(device, target_hue, target_brightness, 15)  # Smooth transition over 15 seconds

async def ocean_scene(lights):
    await lights[4].set().brightness(40).hue_saturation(40, 100).send(lights[4])
    await lights[5].set().brightness(40).hue_saturation(40, 100).send(lights[5])

    await asyncio.gather(
        ocean_effect(lights[0]),
        ocean_effect(lights[1]),
        ocean_effect(lights[2]),
        ocean_effect(lights[3])
    )

async def tavern_scene(lights):
    await lights[4].set().brightness(40).hue_saturation(40, 100).send(lights[4])
    await lights[5].set().brightness(40).hue_saturation(40, 100).send(lights[5])

    await asyncio.gather(
        flicker_candle(lights[0]),
        flicker_candle(lights[1]),
        flicker_candle(lights[2]),
        flicker_candle(lights[3])
    )
