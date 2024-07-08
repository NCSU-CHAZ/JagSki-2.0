from process_Sig1k import process
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

Data = process(
    r"C:\Users\lwlav\OneDrive\Documents\Summer 2024 CHAZ\Data\S103080A004_ICW_test.mat"
)



def RawVel_plotter(Data):

    fig, axs = plt.subplots(4)
    axs[0].plot(
        Data["Burst_Time"],
        np.nanmean(Data["ENU"][:,:,0], axis=1),
        color="green",
        label="East",
    )
    axs[1].plot(
        Data["Burst_Time"],
        np.nanmean(Data["ENU"][:,:,1], axis=1),
        color="red",
        label="North",
    )
    axs[2].plot(
        Data["Burst_Time"],
        np.nanmean(Data["ENU"][:,:,2], axis=1),
        color="blue",
        label="VertVel1",
    )
    axs[3].plot(
        Data["Burst_Time"],
        np.nanmean(Data["ENU"][:,:,3], axis=1),
        color="gray",
        label="VertVel2",
    )
    for i in range(len(axs)):
        axs[i].set_xlim(
            left=dt.datetime(2024, 6, 24, 12, 30), right=dt.datetime(2024, 6, 24, 15, 00)
        )
        axs[i].set_ylim(top=1.5, bottom=-.5)
        axs[i].legend()
    fig.suptitle("Different Velocities versus Time")
    fig.supxlabel("Time (DD HH:MM)")
    fig.supylabel("Velocity (m/s)")
    fig.tight_layout()
    plt.show()


def DepthAvg_plotter(Data):
    plt.figure()
    plt.pcolormesh(
        Data["Burst_Time"],
        Data["CellDepth"],
        Data["ENU"][:,:,1].T,
        vmin=0.3 * np.nanmin(Data["ENU"][:,:,1]),
        vmax=0.3 * np.nanmax(Data["ENU"][:,:,1]),
        shading="nearest",
        cmap="inferno",
    )
    plt.xlim(
        left=dt.datetime(2024, 6, 24, 12, 25), right=dt.datetime(2024, 6, 24, 15, 00)
    )
    plt.xlabel("Date (DD HH:MM)")
    plt.ylabel("Depth m")
    im1 = plt.colorbar()
    im1.ax.set_ylabel("Velocity (m/s)")
    plt.show()


def hist_plotter(Data):
    plt.figure()
    plt.hist(Data["Burst_VelBeam1"][18000:18100])
    plt.show()

RawVel_plotter(Data)

DepthAvg_plotter(Data)

hist_plotter(Data)

