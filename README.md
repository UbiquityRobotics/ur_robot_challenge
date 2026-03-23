# ROS2 Robot Challenge - Avtonomni mobilni roboti (AMR)

Dobrodošli na robotskem izzivu! Ta repozitorij vsebuje začetno programsko kodo za upravljanje mobilnih robotov s sistemom ROS2.
Trenutno vsebuje preprosto vozlišče (`drive_straight`), ki na 100ms pošilja ukaze za premikanje robota naravnost naprej.

## Povezovanje z robotom

## NAVODILA
https://docs.google.com/document/d/12gec_yjAopAPG4-TW27NjqRAmlWTLbvkk2c-xxmtCVM/edit?tab=t.0

Za izvajanje kode na robotu se morate nanj povezati na daljavo prek SSH. Odprite terminal ali Powershell in vpišite:

```bash
ssh ubuntu@<ip_naslov_robota>
```

*(Za točnen IP naslov robota preverite lokalno dokumentacijo, geslo je "ubuntu")*

## Uporaba ros2 paketa na robotu

Ko ste uspešno povezani z robotom, sledite naslednjim korakom za pripravo delovnega okolja:

1. **Pojdite v delovni prostor ROS2 (ROS2 workspace):**
   Običajno se delovni prostor nahaja v `~/ros2_challenge_ws`. Če še ne obstaja, ga prosim ustvarite (ta mapa običajno na robotih že obstaja, vseeno preverite preden ustvarjate nove poti):
   ```bash
   ~/ros2_challenge_ws
   ```

2. **Klonirajte repozitorij:**
   V poddirektorij `src`, klonirajte ta Github repozitorij:
   ```bash
   git clone git@github.com:UbiquityRobotics/ur_robot_challenge.git
   ```

3. **Prevedite paket (Build):**
   Premaknite se nazaj v koren delovnega prostora in zaženite prevajanje paketa z uporabo `colcon`:
   ```bash
   ~/ros2_challenge_ws 
   colcon build --packages-select ur_robot_challenge
   ```

4. **Naložite nastavitve delovnega okolja:**
   Da bo sistem ROS2 prepoznal vaš na novo preveden paket, morate vedno posodobiti okolje:
   ```bash
   source install/setup.bash
   ```

## Zagon vozlišča na robotu

Ko je okolje naloženo, lahko zaženete vozlišče, ki bo robota peljalo naravnost. Zagotovite, da je robot na varnem in ima prosto pot brez ovir!

```bash
ros2 run ur_robot_challenge drive_straight
```

Robot bi se moral začeti premikati naravnost takoj po izvedbi zgornjega ukaza. Za ustavitev pritisnite `Ctrl+C` v terminalu.

## Struktura paketa

* `ur_robot_challenge/drive_straight.py`: Python izvorna koda vozlišča. Naroča in objavlja `Twist` sporočila na temodelu `/cmd_vel`.