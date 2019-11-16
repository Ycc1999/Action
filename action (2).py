import cv2
import time
import math
import pyautogui


def waving_hands(zuobiao,rh_xdzb,reh_xdzb,rh_speed,reh_distance,res_distance,lh_xdzb,leh_xdzb,lh_speed,leh_distance,les_distance,wave_click):

    ###挥手的条件
    ss = 2
    frame_num = 15
    speedlevel = 8
    tolerance = 10
    xtolerance = 10
    ytolerance = 7
    fc = 7

    if zuobiao[4] != (0, 0) and zuobiao[1] != (0, 0) and zuobiao[3] != (0, 0):
        if len(rh_xdzb) < 2 or len(reh_distance) < ss+1:
            rh_xdzb.append((zuobiao[4][0] - zuobiao[1][0], zuobiao[4][1] - zuobiao[1][1]))
            reh_distance.append((zuobiao[3][0] - zuobiao[4][0], zuobiao[3][1] - zuobiao[4][1]))
            res_distance.append((zuobiao[3][0] - zuobiao[2][0], zuobiao[3][1] - zuobiao[2][1]))
        else:
            del rh_xdzb[0]
            del reh_distance[0]
            del res_distance[0]
            rh_xdzb.append((zuobiao[4][0] - zuobiao[1][0], zuobiao[4][1] - zuobiao[1][1]))
            reh_distance.append((zuobiao[3][0] - zuobiao[4][0], zuobiao[3][1] - zuobiao[4][1]))
            res_distance.append((zuobiao[3][0] - zuobiao[2][0], zuobiao[3][1] - zuobiao[2][1]))

            res_xdistance = [res_distance[i][0] for i in range(ss+1)]
            avrage_res_xdistance = sum(res_xdistance)/len(res_xdistance)
            res_xdistance_change = [(res_distance[i + 1][0] - res_distance[i][0]) ** 2 for i in range(ss)]
            res_xdistance_fx = math.sqrt(sum(res_xdistance_change) / ss)

            reh_xdistance_change = [(reh_distance[i+1][0]-reh_distance[i][0])**2 for i in range(ss)]
            reh_xdistance_fx = math.sqrt(sum(reh_xdistance_change)/ss)

            reh_ydistance_change = [(reh_distance[i+1][1]-reh_distance[i][1])**2 for i in range(ss)]
            reh_ydistance_fx = math.sqrt(sum(reh_ydistance_change)/ss)

            yreh_distance = [abs(reh_distance[i][1]) for i in range(ss + 1)]
            average_yreh_distance = sum(yreh_distance) / len(yreh_distance)

            if len(rh_speed) < ss:
                rh_speed.append((rh_xdzb[1][0] - rh_xdzb[0][0], rh_xdzb[1][1] - rh_xdzb[0][1]))
            else:
                del rh_speed[0]
                rh_speed.append((rh_xdzb[1][0] - rh_xdzb[0][0], rh_xdzb[1][1] - rh_xdzb[0][1]))

                rh_speedx = [rh_speed[i][0] for i in range(ss)]
                rh_speedy = [rh_speed[i][1] for i in range(ss)]

                rhaspeedx = abs(sum(rh_speedx) / ss)
                rhaspeedy = abs(sum(rh_speedy) / ss)

                if rhaspeedx > speedlevel and reh_ydistance_fx < fc and average_yreh_distance < ytolerance:
                    if  reh_distance[0][0] > 3 and reh_distance[ss][0] < -3 and min(rh_speedx) > 0:
                        if wave_click == frame_num:
                            print("left click")
                            wave_click = 0

                    elif reh_distance[0][0] < -3 and reh_distance[ss][0] > 3 and max(rh_speedx) < 0:
                        if wave_click == frame_num:
                            print("right click")
                            wave_click = 0

                elif rhaspeedy > speedlevel and reh_xdistance_fx < fc + 1 and avrage_res_xdistance > 5 and res_xdistance_fx < fc - 1:
                    if min(rh_speedy) > 0:
                        if wave_click == frame_num:
                            print("down click")
                            wave_click = 0

                    '''
                    elif max(rh_speedy) < 0 :
                        if click_num == frame_num:
                            print("up click")
                            wave_click = 0
                    '''

    if zuobiao[7] != (0, 0) and zuobiao[1] != (0, 0):
        if len(lh_xdzb) < 2 or len(leh_distance) < ss+1:
            lh_xdzb.append((zuobiao[7][0] - zuobiao[1][0], zuobiao[7][1] - zuobiao[1][1]))
            leh_distance.append((zuobiao[6][0] - zuobiao[7][0], zuobiao[6][1] - zuobiao[7][1]))
            les_distance.append((zuobiao[6][0] - zuobiao[5][0], zuobiao[6][1] - zuobiao[5][1]))
        else:
            del lh_xdzb[0]
            del leh_distance[0]
            del les_distance[0]

            lh_xdzb.append((zuobiao[7][0] - zuobiao[1][0], zuobiao[7][1] - zuobiao[1][1]))
            leh_distance.append((zuobiao[6][0] - zuobiao[7][0], zuobiao[6][1] - zuobiao[7][1]))
            les_distance.append((zuobiao[6][0] - zuobiao[5][0], zuobiao[6][1] - zuobiao[5][1]))

            yleh_distance = [abs(leh_distance[i][1]) for i in range(ss + 1)]
            xles_distance = [abs(leh_distance[i][0]) for i in range(ss + 1)]

            average_yleh_distance = sum(yleh_distance) / len(yleh_distance)
            average_xles_distance = sum(xles_distance) / len(xles_distance)

            if len(lh_speed) < ss:
                lh_speed.append((lh_xdzb[1][0] - lh_xdzb[0][0], lh_xdzb[1][1] - lh_xdzb[0][1]))
            else:
                del lh_speed[0]
                lh_speed.append((lh_xdzb[1][0] - lh_xdzb[0][0], lh_xdzb[1][1] - lh_xdzb[0][1]))

                lh_speedx = [lh_speed[i][0] for i in range(ss)]
                lh_speedy = [lh_speed[i][1] for i in range(ss)]

                lhaspeedx = abs(sum(lh_speedx) / ss)
                lhaspeedy = abs(sum(lh_speedy) / ss)

                lh_total_x = 0
                lh_total_y = 0

                for i in range(ss):
                    lh_total_x = lh_total_x + abs(lh_speed[i][0])
                    lh_total_y = lh_total_y + abs(lh_speed[i][1])

                if max(lh_speedx)*min(lh_speedx) > 0 and lh_total_y < tolerance and lhaspeedx > speedlevel:
                    if min(lh_speedx) > 0 and average_yleh_distance < ytolerance:
                        if wave_click == frame_num:
                            print("left click")
                            wave_click = 0

                    elif max(lh_speedx) < 0 and average_yleh_distance < ytolerance:
                        if wave_click == frame_num:
                            print("right click")
                            wave_click = 0

                elif max(lh_speedy) * min(lh_speedy) > 0 and lh_total_x < tolerance and lhaspeedy > speedlevel:
                    if min(lh_speedy) > 0 and average_xles_distance > xtolerance:
                        if wave_click == frame_num:
                            print("down click")
                            wave_click = 0

                    '''
                    elif max(lh_speedy) < 0 and average_xles_distance > xtolerance:
                        if wave_click == frame_num:
                            print("up click")
                            wave_click = 0
                    '''
    if wave_click < frame_num:
        wave_click = wave_click + 1

    return rh_xdzb,reh_xdzb,rh_speed,reh_distance,res_distance,lh_xdzb,leh_xdzb,lh_speed,leh_distance,les_distance,wave_click

def falling(zuobiao,fall_click, jlsdH, jlsdH5, jlsdW, stature, ave_statu):

    ###摔倒
    fc1 = 0
    Hv = 0.1
    Wv = 0.02
    HcompareW = 1.2
    frame_num = 15

    sdzuobiao = zuobiao
    del sdzuobiao[4]
    del sdzuobiao[7]
    # 删掉两个手
    sdzb_x = [sdzuobiao[i][0] for i in range(len(sdzuobiao))]
    sdzb_y = [sdzuobiao[i][1] for i in range(len(sdzuobiao))]

    maxsd_x = max(sdzb_x)
    minsd_x = min(sdzb_x)
    maxsd_y = max(sdzb_y)
    minsd_y = min(sdzb_y)

    sdH = maxsd_y - minsd_y
    sdW = maxsd_x - minsd_x
    # 框出人的长宽

    if len(stature) < 5:
        if sdH / sdW > 0.5:  ##
            stature.append(sdH)
            # 记下人的高
    else:  # 已经开始了一段时间
        if sdH / sdW > 0.5:  ##
            del stature[0]
            # 删除最老的
            stature.append(sdH)
            # 加上新的高
            ave_statu1 = sum(stature) / len(stature)
            for i in stature:
                fc1 = (i - ave_statu1) ** 2 + fc1
            fc = (fc1 / len(stature)) ** 0.5
            if fc < 10:  ##
                ave_statu = sum(stature) / len(stature)
                # 根据5帧的平均值来算人的平均身高

    if sdH / sdW < HcompareW and len(stature) == 5:  # 人的长宽是否小于一定比例，如果小于，进行人有没有下降的判断

        if len(jlsdH) < 2 or len(jlsdW) < 2:  # 如果是最开始，长度小于2
            jlsdH.append(sdH)
            # 记下人的高
            jlsdW.append(sdW)
            # 记下人的宽
        else:  # 已经开始了一段时间
            del jlsdH[0]
            del jlsdW[0]
            # 删除最老的
            jlsdH.append(sdH)
            jlsdW.append(sdW)
            # 加上新的长宽
            sdHspeed = jlsdH[1] - jlsdH[0]
            sdWspeed = jlsdW[1] - jlsdW[0]
            # 根据两帧来算纵向横向速度
            if sdHspeed / ave_statu < -Hv and sdWspeed / ave_statu > Wv and fall_click == frame_num:  # 人纵向有没有达到下降的速度（负），横向速度是否达到（正）
                print('sd')
                fall_click = 0

    if fall_click < frame_num:
        fall_click = fall_click + 1

    return fall_click, jlsdH, jlsdH5, jlsdW, stature, ave_statu


