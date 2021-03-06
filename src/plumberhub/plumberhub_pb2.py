# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlumberHub.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='PlumberHub.proto',
    package='Plumber',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x10PlumberHub.proto\x12\x07Plumber\"J\n\x06Sample\x12\n\n\x02\x61t\x18\x01 \x01(\x04\x12\x13\n\x0bmicrosecond\x18\x02 \x01(\r\x12\r\n\x05\x65vent\x18\x03 \x01(\r\x12\x10\n\x08\x64\x61taList\x18\x04 \x03(\x11\x62\x06proto3')
)

_SAMPLE = _descriptor.Descriptor(
    name='Sample',
    full_name='Plumber.Sample',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='at', full_name='Plumber.Sample.at', index=0,
            number=1, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='microsecond', full_name='Plumber.Sample.microsecond', index=1,
            number=2, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='event', full_name='Plumber.Sample.event', index=2,
            number=3, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='dataList', full_name='Plumber.Sample.dataList', index=3,
            number=4, type=17, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=29,
    serialized_end=103,
)

DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), {
    'DESCRIPTOR': _SAMPLE,
    '__module__': 'PlumberHub_pb2'
    # @@protoc_insertion_point(class_scope:Plumber.Sample)
})
_sym_db.RegisterMessage(Sample)

# @@protoc_insertion_point(module_scope)
