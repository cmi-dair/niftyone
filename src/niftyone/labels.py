"""
Custom labels used in the niftyone dashboard
"""

import fiftyone.core.fields as fof
from fiftyone.core.labels import Label


class MRIQCT1w(Label):
    """
    MRIQC T1w IQMs
    """

    cjv = fof.FloatField()
    cnr = fof.FloatField()
    efc = fof.FloatField()
    fber = fof.FloatField()
    fwhm_avg = fof.FloatField()
    fwhm_x = fof.FloatField()
    fwhm_y = fof.FloatField()
    fwhm_z = fof.FloatField()
    icvs_csf = fof.FloatField()
    icvs_gm = fof.FloatField()
    icvs_wm = fof.FloatField()
    inu_med = fof.FloatField()
    inu_range = fof.FloatField()
    qi_1 = fof.FloatField()
    qi_2 = fof.FloatField()
    rpve_csf = fof.FloatField()
    rpve_gm = fof.FloatField()
    rpve_wm = fof.FloatField()
    size_x = fof.FloatField()
    size_y = fof.FloatField()
    size_z = fof.FloatField()
    snr_csf = fof.FloatField()
    snr_gm = fof.FloatField()
    snr_total = fof.FloatField()
    snr_wm = fof.FloatField()
    snrd_csf = fof.FloatField()
    snrd_gm = fof.FloatField()
    snrd_total = fof.FloatField()
    snrd_wm = fof.FloatField()
    spacing_x = fof.FloatField()
    spacing_y = fof.FloatField()
    spacing_z = fof.FloatField()
    tpm_overlap_csf = fof.FloatField()
    tpm_overlap_gm = fof.FloatField()
    tpm_overlap_wm = fof.FloatField()
    wm2max = fof.FloatField()


class MRIQCBold(Label):
    """
    MRIQC BOLD IQMs
    """

    aor = fof.FloatField()
    aqi = fof.FloatField()
    dummy_trs = fof.FloatField()
    dvars_nstd = fof.FloatField()
    dvars_std = fof.FloatField()
    dvars_vstd = fof.FloatField()
    efc = fof.FloatField()
    fber = fof.FloatField()
    fd_mean = fof.FloatField()
    fd_num = fof.FloatField()
    fd_perc = fof.FloatField()
    fwhm_avg = fof.FloatField()
    fwhm_x = fof.FloatField()
    fwhm_y = fof.FloatField()
    fwhm_z = fof.FloatField()
    gcor = fof.FloatField()
    gsr_x = fof.FloatField()
    gsr_y = fof.FloatField()
    size_t = fof.FloatField()
    size_x = fof.FloatField()
    size_y = fof.FloatField()
    size_z = fof.FloatField()
    snr = fof.FloatField()
    spacing_tr = fof.FloatField()
    spacing_x = fof.FloatField()
    spacing_y = fof.FloatField()
    spacing_z = fof.FloatField()
    tsnr = fof.FloatField()
