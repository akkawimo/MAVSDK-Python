# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import winch_pb2, winch_pb2_grpc
from enum import Enum


class WinchAction(Enum):
    """
 

     Values
     ------
     RELAXED
         
     RELATIVE_LENGTH_CONTROL
         
     RATE_CONTROL
         
     LOCK
         
     DELIVER
         
     HOLD
         
     RETRACT
         
     LOAD_LINE
         
     ABANDON_LINE
         
     LOAD_PAYLOAD
         
     """

    
    RELAXED = 0
    RELATIVE_LENGTH_CONTROL = 1
    RATE_CONTROL = 2
    LOCK = 3
    DELIVER = 4
    HOLD = 5
    RETRACT = 6
    LOAD_LINE = 7
    ABANDON_LINE = 8
    LOAD_PAYLOAD = 9

    def translate_to_rpc(self):
        if self == WinchAction.RELAXED:
            return winch_pb2.WINCH_ACTION_RELAXED
        if self == WinchAction.RELATIVE_LENGTH_CONTROL:
            return winch_pb2.WINCH_ACTION_RELATIVE_LENGTH_CONTROL
        if self == WinchAction.RATE_CONTROL:
            return winch_pb2.WINCH_ACTION_RATE_CONTROL
        if self == WinchAction.LOCK:
            return winch_pb2.WINCH_ACTION_LOCK
        if self == WinchAction.DELIVER:
            return winch_pb2.WINCH_ACTION_DELIVER
        if self == WinchAction.HOLD:
            return winch_pb2.WINCH_ACTION_HOLD
        if self == WinchAction.RETRACT:
            return winch_pb2.WINCH_ACTION_RETRACT
        if self == WinchAction.LOAD_LINE:
            return winch_pb2.WINCH_ACTION_LOAD_LINE
        if self == WinchAction.ABANDON_LINE:
            return winch_pb2.WINCH_ACTION_ABANDON_LINE
        if self == WinchAction.LOAD_PAYLOAD:
            return winch_pb2.WINCH_ACTION_LOAD_PAYLOAD

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RELAXED:
            return WinchAction.RELAXED
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RELATIVE_LENGTH_CONTROL:
            return WinchAction.RELATIVE_LENGTH_CONTROL
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RATE_CONTROL:
            return WinchAction.RATE_CONTROL
        if rpc_enum_value == winch_pb2.WINCH_ACTION_LOCK:
            return WinchAction.LOCK
        if rpc_enum_value == winch_pb2.WINCH_ACTION_DELIVER:
            return WinchAction.DELIVER
        if rpc_enum_value == winch_pb2.WINCH_ACTION_HOLD:
            return WinchAction.HOLD
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RETRACT:
            return WinchAction.RETRACT
        if rpc_enum_value == winch_pb2.WINCH_ACTION_LOAD_LINE:
            return WinchAction.LOAD_LINE
        if rpc_enum_value == winch_pb2.WINCH_ACTION_ABANDON_LINE:
            return WinchAction.ABANDON_LINE
        if rpc_enum_value == winch_pb2.WINCH_ACTION_LOAD_PAYLOAD:
            return WinchAction.LOAD_PAYLOAD

    def __str__(self):
        return self.name


class WinchResult:
    """
     Result type.

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for action requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request was successful

         NO_SYSTEM
              No system is connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command refused by vehicle

         COMMAND_DENIED_LANDED_STATE_UNKNOWN
              Command refused because landed state is unknown

         COMMAND_DENIED_NOT_LANDED
              Command refused because vehicle not landed

         TIMEOUT
              Request timed out

         VTOL_TRANSITION_SUPPORT_UNKNOWN
              Hybrid/VTOL transition support is unknown

         NO_VTOL_TRANSITION_SUPPORT
              Vehicle does not support hybrid/VTOL transitions

         PARAMETER_ERROR
              Error getting or setting parameter

         UNSUPPORTED
              Action not supported

         FAILED
              Action failed

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        COMMAND_DENIED_LANDED_STATE_UNKNOWN = 6
        COMMAND_DENIED_NOT_LANDED = 7
        TIMEOUT = 8
        VTOL_TRANSITION_SUPPORT_UNKNOWN = 9
        NO_VTOL_TRANSITION_SUPPORT = 10
        PARAMETER_ERROR = 11
        UNSUPPORTED = 12
        FAILED = 13

        def translate_to_rpc(self):
            if self == WinchResult.Result.UNKNOWN:
                return winch_pb2.WinchResult.RESULT_UNKNOWN
            if self == WinchResult.Result.SUCCESS:
                return winch_pb2.WinchResult.RESULT_SUCCESS
            if self == WinchResult.Result.NO_SYSTEM:
                return winch_pb2.WinchResult.RESULT_NO_SYSTEM
            if self == WinchResult.Result.CONNECTION_ERROR:
                return winch_pb2.WinchResult.RESULT_CONNECTION_ERROR
            if self == WinchResult.Result.BUSY:
                return winch_pb2.WinchResult.RESULT_BUSY
            if self == WinchResult.Result.COMMAND_DENIED:
                return winch_pb2.WinchResult.RESULT_COMMAND_DENIED
            if self == WinchResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN:
                return winch_pb2.WinchResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if self == WinchResult.Result.COMMAND_DENIED_NOT_LANDED:
                return winch_pb2.WinchResult.RESULT_COMMAND_DENIED_NOT_LANDED
            if self == WinchResult.Result.TIMEOUT:
                return winch_pb2.WinchResult.RESULT_TIMEOUT
            if self == WinchResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return winch_pb2.WinchResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN
            if self == WinchResult.Result.NO_VTOL_TRANSITION_SUPPORT:
                return winch_pb2.WinchResult.RESULT_NO_VTOL_TRANSITION_SUPPORT
            if self == WinchResult.Result.PARAMETER_ERROR:
                return winch_pb2.WinchResult.RESULT_PARAMETER_ERROR
            if self == WinchResult.Result.UNSUPPORTED:
                return winch_pb2.WinchResult.RESULT_UNSUPPORTED
            if self == WinchResult.Result.FAILED:
                return winch_pb2.WinchResult.RESULT_FAILED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_UNKNOWN:
                return WinchResult.Result.UNKNOWN
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_SUCCESS:
                return WinchResult.Result.SUCCESS
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_NO_SYSTEM:
                return WinchResult.Result.NO_SYSTEM
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_CONNECTION_ERROR:
                return WinchResult.Result.CONNECTION_ERROR
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_BUSY:
                return WinchResult.Result.BUSY
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_COMMAND_DENIED:
                return WinchResult.Result.COMMAND_DENIED
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN:
                return WinchResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_COMMAND_DENIED_NOT_LANDED:
                return WinchResult.Result.COMMAND_DENIED_NOT_LANDED
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_TIMEOUT:
                return WinchResult.Result.TIMEOUT
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return WinchResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_NO_VTOL_TRANSITION_SUPPORT:
                return WinchResult.Result.NO_VTOL_TRANSITION_SUPPORT
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_PARAMETER_ERROR:
                return WinchResult.Result.PARAMETER_ERROR
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_UNSUPPORTED:
                return WinchResult.Result.UNSUPPORTED
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_FAILED:
                return WinchResult.Result.FAILED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the WinchResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two WinchResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # WinchResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ WinchResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"WinchResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcWinchResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return WinchResult(
                
                WinchResult.Result.translate_from_rpc(rpcWinchResult.result),
                
                
                rpcWinchResult.result_str
                )

    def translate_to_rpc(self, rpcWinchResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcWinchResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcWinchResult.result_str = self.result_str
            
        
        



class WinchError(Exception):
    """ Raised when a WinchResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Winch(AsyncBase):
    """
 

     Generated by dcsdkgen - MAVSDK Winch API
    """

    # Plugin name
    name = "Winch"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = winch_pb2_grpc.WinchServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return WinchResult.translate_from_rpc(response.winch_result)
    

    async def relax(self, instance):
        """
         Allow motor to freewheel.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RelaxRequest()
        request.instance = instance
        response = await self._stub.Relax(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "relax()", instance)
        

    async def relative_length_control(self, instance, length, rate):
        """
         Wind or unwind specified length of line, optionally using specified rate.

         Parameters
         ----------
         instance : uint32_t
             
         length : float
             
         rate : float
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RelativeLengthControlRequest()
        request.instance = instance
        request.length = length
        request.rate = rate
        response = await self._stub.RelativeLengthControl(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "relative_length_control()", instance, length, rate)
        

    async def rate_control(self, instance, rate):
        """
         Wind or unwind line at specified rate.

         Parameters
         ----------
         instance : uint32_t
             
         rate : float
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RateControlRequest()
        request.instance = instance
        request.rate = rate
        response = await self._stub.RateControl(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "rate_control()", instance, rate)
        

    async def lock(self, instance):
        """
         Perform the locking sequence to relieve motor while in the fully retracted position.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.LockRequest()
        request.instance = instance
        response = await self._stub.Lock(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "lock()", instance)
        

    async def deliver(self, instance):
        """
         Sequence of drop, slow down, touch down, reel up, lock.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.DeliverRequest()
        request.instance = instance
        response = await self._stub.Deliver(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "deliver()", instance)
        

    async def hold(self, instance):
        """
         Engage motor and hold current position.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.HoldRequest()
        request.instance = instance
        response = await self._stub.Hold(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "hold()", instance)
        

    async def retract(self, instance):
        """
         Return the reel to the fully retracted position.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RetractRequest()
        request.instance = instance
        response = await self._stub.Retract(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "retract()", instance)
        

    async def load_line(self, instance):
        """
         Load the reel with line.

         The winch will calculate the total loaded length and stop when the tension exceeds a threshold.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.LoadLineRequest()
        request.instance = instance
        response = await self._stub.LoadLine(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "load_line()", instance)
        

    async def abandon_line(self, instance):
        """
         Spool out the entire length of the line.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.AbandonLineRequest()
        request.instance = instance
        response = await self._stub.AbandonLine(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "abandon_line()", instance)
        

    async def load_payload(self, instance):
        """
         Spools out just enough to present the hook to the user to load the payload.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.LoadPayloadRequest()
        request.instance = instance
        response = await self._stub.LoadPayload(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "load_payload()", instance)
        