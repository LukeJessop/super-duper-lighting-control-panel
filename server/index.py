import asyncio
import LightingControl

async def main():
    tapo_username = "kirby.balding@aol.com"
    tapo_password = "enMe7bsz!"

    client = LightingControl.ApiClient(tapo_username, tapo_password)
    light_1 = await client.l530("192.168.0.12")
    light_2 = await client.l530("192.168.0.144")
    light_3 = await client.l530("192.168.0.212")
    light_4 = await client.l530("192.168.0.84")
    light_5 = await client.l530("192.168.0.70")
    light_6 = await client.l530("192.168.0.149")

    lights = [light_1, light_2, light_3, light_4, light_5, light_6]

    await LightingControl.lights_on(lights)

    await LightingControl.tavern_scene(lights)

    await LightingControl.lights_off(lights)

if __name__ == "__main__":
    asyncio.run(main())