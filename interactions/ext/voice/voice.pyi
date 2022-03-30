import interactions
from interactions.api.models.presence import ClientPresence
from interactions.models.command import Option
from interactions.api.models.misc import MISSING, DictSerializerMixin, Snowflake
from typing import Optional, Union, Tuple, Dict, Any, List
from datetime import datetime
from interactions.api.models.member import Member
from interactions.api.models.guild import Guild
from interactions.api.models.channel import Channel
from interactions.api.gateway import WebSocketClient
from interactions.api.cache import Cache, Storage
from interactions.api.http.client import HTTPClient

class VoiceCache(Cache):
    def __init__(self): ...
    voice_states: Storage

class VoiceConnectionWebSocketClient:

    _close: bool
    _closed: bool

    async def _send_packet(self, data: Dict[str, Any]) -> None: ...
    ...

class VoiceWebSocketClient(WebSocketClient):
    def __init__(
        self,
        token,
        intents,
        session_id=MISSING,
        sequence=MISSING,
    ) -> None: ...
    __voice_connect_data: Dict[int, dict]
    _voice_connections: Dict[int, VoiceConnectionWebSocketClient]

    def __contextualize(self, data: dict) -> object: ...
    def __sub_command_context(
        self, data: Union[dict, Option], context: object
    ) -> Union[Tuple[str], dict]: ...
    def __option_type_context(self, context: object, type: int) -> dict: ...
    async def _handle_connection(
        self,
        stream: Dict[str, Any],
        shard: Optional[List[Tuple[int]]] = MISSING,
        presence: Optional[ClientPresence] = MISSING,
    ) -> None: ...
    def _dispatch_event(self, event: str, data: dict) -> None: ...
    async def _connect(
        self,
        guild_id: int,
        channel_id: int,
        self_mute: bool = False,
        self_deaf: bool = False,
    ) -> None: ...
    async def _disconnect(
        self,
        guild_id: int
    ) -> None: ...

class VoiceState(DictSerializerMixin):
    _client: HTTPClient
    _json: dict
    channel_id: Optional[Snowflake]
    guild_id: Optional[Snowflake]
    user_id: Snowflake
    member: Optional[Member]
    mute: bool
    deaf: bool
    self_video: bool
    self_mute: bool
    self_deaf: bool
    self_stream: Optional[bool]
    suppress: bool
    session_id: str
    request_to_speak_timestamp: Optional[datetime]

    @property
    def before(self) -> VoiceState: ...
    async def mute_member(self, reason: Optional[str]) -> Member: ...
    async def deafen_member(self, reason: Optional[str]) -> Member: ...
    async def move_member(self, channel_id: int, *, reason: Optional[str]) -> Member: ...
    async def get_channel(self) -> Channel: ...
    async def get_guild(self) -> Guild: ...

def setup(client: interactions.Client, voice_client: bool = False): ...
