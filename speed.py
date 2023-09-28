# import the library
import flet as ft
import speedtest
from time import sleep

# use the main function
def main(page: ft.Page):
    #window
    page.window_max_width=580
    page.window_max_height=740
    
    # setting up the page
    page.title = 'Speed Test'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_bgcolor = 'blue'
    page.padding = 30
    # enable scroll page
    page.auto_scroll = True

    # font
    page.fonts = {
        'hack': 'fonts/Hack-BoldItalic.ttf',
        'speedy': 'fonts/Speedy Marker Italic.ttf',
        'fun-game': 'fonts/Fun-Games.otf',
        'fast': 'fonts/Fast Hand.otf',
        'speed': 'fonts/SpeedBeast FREE.ttf'
    }
    
    # initializing the speedtest variable
    st = speedtest.Speedtest(secure=True)
    
    # teks
    line_01=ft.Text(value='> Press Start...', font_family='hack',color='white')
    line_02=ft.Text(value='', font_family='hack',color='#60e354')
    line_03=ft.Text(value='', font_family='hack',color='#60e354')
    pb_01 = ft.ProgressBar(width=400,color="#0080ff", bgcolor="#eeeeee", opacity=0)
    line_04=ft.Text(value='', font_family='hack',color='#e3e354')
    line_05=ft.Text(value='', font_family='hack',color='#60e354')
    line_06=ft.Text(value='', font_family='hack',color='#60e354')
    pb_02 = ft.ProgressBar(width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    line_07=ft.Text(value='', font_family='hack',color='#e3e354')
    line_08=ft.Text(value='', font_family='hack',color='white')
    line_09=ft.Text(value='', font_family='hack',color='white')
    terminalText=ft.Column([line_01,line_02,line_03,pb_01,line_04,line_05,line_06,pb_02,line_07,line_08,line_09])
    
    
    # container
    getSpeedContainer = ft.Container(
        content=terminalText,
        width=400,
        height=100,
        bgcolor='grey',
        border_radius=20,
        padding=20,
        animate=ft.animation.Animation(1000, 'bounceOut')
    )
    
    def animated_getSpeedContainer(e):
        # Repeat
        pb_01.opacity=0
        pb_01.opacity=0
        pb_01.value=None
        pb_02.opacity=0
        pb_02.opacity=0
        pb_02.value=None
        line_01.value=''
        line_02.value=''
        line_03.value=''
        line_04.value=''
        line_05.value=''
        line_06.value=''
        line_07.value=''
        line_08.value=''
        line_09.value=''
        
        getSpeedContainer.update()
        getSpeedContainer.width = 800
        getSpeedContainer.height = 400
        line_01.value='> calculating download speed, please wait'
        getSpeedContainer.update()
        sleep(1)
        
        ideal_server=st.get_best_server()
        city=ideal_server['name']
        country=ideal_server['country']
        cc=ideal_server['cc']
        line_02.value=f'> finding the possible server in {city} {country} ({cc})'
        getSpeedContainer.update()
        sleep(1)
        
        line_03.value='> connection established, status OK, fetching download speed'
        pb_01.opacity=1
        pb_01.opacity=1
        getSpeedContainer.update()
        donwload_speed=st.download()/1024/1024 # byte/sec to Mbps
        pb_01.value=1
        line_04.value=f'> the download speed is {str(round(donwload_speed,2))} Mbps'
        getSpeedContainer.update()
        sleep(1)
        
        
        line_05.value='> calculating upload speed, please wait'
        getSpeedContainer.update()
        sleep(0.5)
        
        line_06.value='> executing upload script, hold on'
        getSpeedContainer.update()
        sleep(0.5)
        
        pb_02.opacity=1
        pb_02.opacity=1
        getSpeedContainer.update()
        upload_speed=st.upload()/1024/1024 # byte/sec to Mbps
        pb_02.value=1
        line_07.value=f'> the upload speed is {str(round(upload_speed,2))} Mbps'
        getSpeedContainer.update()
        sleep(1)
        
        line_08.value='> task completed succesfully'
        line_09.value='>> app developer: Yudhy Prayitno'
        getSpeedContainer.update()
        
    # text
    appTitle = ft.Row(
        controls=[
            ft.Text('Internet', font_family='speed', color='#dc3124', size=55),
            ft.Text('Speed', font_family='speed', color='#5967ff', size=55)
        ],
        alignment='center',
    )

    # page components
    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, icon_size=40, icon_color='#0abab5', on_click=animated_getSpeedContainer)
    )

ft.app(target=main, assets_dir='assets')
