#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""DW1000: A fully integrated single chip Ultra Wideband (UWB) low-power low-cost transceiver IC for 2-way ranging or TDOA location systems."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Decawave"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from DW1000_constants import *

# name:        DW1000
# description: A fully integrated single chip Ultra Wideband (UWB) low-power low-cost transceiver IC for 2-way ranging or TDOA location systems.
# manuf:       Decawave
# version:     0.1
# url:         http://www.decawave.com/support/download/file/nojs/796
# date:        2017-02-07


# Derive from this class and implement read and write
class DW1000_Base:
	"""A fully integrated single chip Ultra Wideband (UWB) low-power low-cost transceiver IC for 2-way ranging or TDOA location systems."""
	# Register DEV_ID
	# 7.2.2
	#       Register 0x00 is the device identifier.
	#       This is hard-coded into the silicon.
	#       The value in this register is read-only and cannot be overwritten by the host system.
	#       The device ID will be changed for any silicon updates.
	#       The device ID register is ideal to use in the host μP to validate that the SPI interface
	#       is operational.
	#       It is expected that the host system will validate that the device ID is the expected
	#       value, supported by its software, before proceeding to use the IC. 
	
	
	def setDEV_ID(self, val):
		"""Set register DEV_ID"""
		self.write(REG.DEV_ID, val, 8)
	
	def getDEV_ID(self):
		"""Get register DEV_ID"""
		return self.read(REG.DEV_ID, 8)
	
	# Bits DEV_ID
	# Register SYS_CFG
	# 7.2.6
	#       Register 0x04 is the system configuration register.
	#       This is a bitmapped register.
	#       Each bit field is separately identified and described below.
	#       The System Configuration register contains the following bitmapped sub-fields: Definition
	#       of the bit fields within REG:04:00 – SYS_CFG: System Configuration bitmap: - 
	
	
	def setSYS_CFG(self, val):
		"""Set register SYS_CFG"""
		self.write(REG.SYS_CFG, val, 8)
	
	def getSYS_CFG(self):
		"""Get register SYS_CFG"""
		return self.read(REG.SYS_CFG, 8)
	
	# Bits SYS_CFG
	# Register TX_FCTRL
	# 7.2.10
	#       Register 0x08, the transmit frame control register, contains a number of TX control fields.
	#       (For a general discussion of transmission please refer to section 3 – Message Transmission.) 
	
	
	def setTX_FCTRL(self, val):
		"""Set register TX_FCTRL"""
		self.write(REG.TX_FCTRL, val, 8)
	
	def getTX_FCTRL(self):
		"""Get register TX_FCTRL"""
		return self.read(REG.TX_FCTRL, 8)
	
	# Bits TX_FCTRL
