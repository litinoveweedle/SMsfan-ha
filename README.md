# Sequent Microsystems Smart Fan Home Assistant Integration

Integrate [Smart Fan](https://sequentmicrosystems.com/products/smart-fan-hat-for-raspberry-pi)
seamlessly with Home Assistant, bringing all your custom functionality into the Home Assistant ecosystem for enhanced control, automation, and ease of use.



## Installation

> This development version requires `SMcommonHA>=0.0.2`, which must be
> published before deployment. All installed Sequent integration pins should be
> updated and tested together.

> If you already have HACS, I2C and File editor configured, you can skip to [The actual installation](#the-actual-installation)


#### Video tutorials

- [Install HACS video](https://youtu.be/Fl3lATWhQVM) for step 1.
- [Enable I2C and Install file editor video](https://youtu.be/53Zj8NofS7k) for steps 2. and 3.
- [Install and config card drivers video](https://youtu.be/yH2HKjm7j24) for steps 4. and 5.

#### Prerequirements

1. Install HACS
    - Follow the official [instructions](https://www.hacs.xyz/docs/use/download/download/)

2. Install and run HassOS I2C Configurator add-on
    - Install [HassOS I2C Configurator](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fadamoutler%2FHassOSConfigurator)
    - Select your profile from the buttom left corner and enable `Advanced mode` in User settings
    - In Settings, Add-ons, Add-on Store, search and install `HassOS I2C Configurator`
    - Disable `Protection mode`
    - Start the add-on

3. Install File editor add-on
    - In Settings, Add-ons, Add-on Store, search and install `File editor`
    - Enable `Show in sidebar`
(see multiple config options bellow)


### The actual installation

4. Install SMsfan-ha from HACS
    - Open HACS (from the sidebar)
    - Click on the 3 dots in the top right corner and select `Custom repositories`
    - Repository is `SequentMicrosystems/SMsfan-ha` and type is `Integration`
    - Once added, you can now search it in HACS menu and download it

5. Restart Home Assistant, then open **Settings > Devices & services**.
6. Select **Add integration**, choose **Sequent Microsystems Smart Fan Integration**, and enter the
   card's stack address. Repeat for each card.
7. Use **Configure** to choose entities and their update intervals.

### Upgrading from `SMsfan`

Back up Home Assistant first. Uninstall the old integration and install the
updated one; Marketplace may require re-adding the repository. Ensure
`custom_components/SMsfan` is removed and only `custom_components/smsfan`
remains. Change the top-level `SMsfan:` YAML key to `smsfan:` and restart.
Existing entity registry entries are migrated to the new domain; conflicting
entries must be resolved before setup can continue.

## Migrating from YAML

Existing `smsfan:` YAML is imported once. Check the entries under **Settings >
Devices & services**, remove the YAML section and restart Home Assistant. Later
YAML edits are not imported, and existing entries are not overwritten. Use the
integration UI for further changes.

The legacy examples below are retained for reference:

`configuration.yaml` example:
```yaml
# Loads default set of integrations. Do not remove.
default_config:

# Load frontend themes from the themes folder
frontend:
  themes: !include_dir_merge_named themes

automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml

smsfan:
    # + optional configs
```

- Simple stack 0 config:

```yaml
smsfan:
```

- Specific stack config:

```yaml
smsfan:
    - stack: 2
```

- Multiple cards on different stack levels:

```yaml
smsfan:
    - stack: 0
    - stack: 2
    - stack: 3
```

- Only specific entities for different stack levels:

> The following example is provided for illustrative purposes only and does not necessarily represent real entities.

```yaml
smsfan:
    - stack: 0
      relay_1:
      relay_3:
      opto_1:
        update_interval: 0.1
    - stack: 2
      relay:
        chan_range: "1..8"
      opto_cnt:
        chan_range: "2..6"
        update_interval: 1
```

[//]: # (__CUSTOM_README__ START)
[//]: # (__CUSTOM_README__ END)

### `configuration.yaml` entities

Possible entities:
```
power_1: (type: number)
```

Entity options:
- `chan_range: "start..end"` (specify inclusive channel range)
- `update_interval: seconds` (specify the update interval for `sensor` and `binary_sensor`, default 30s)

## Testing

With Python 3.14, install `homeassistant==2026.11.1`,
`pytest-homeassistant==2026.11.1`, and the integration requirements from the
manifest, then run:

```shell
python -m pytest -p no:respx --asyncio-mode=auto -o asyncio_default_fixture_loop_scope=function tests
```

Tests simulate hardware and check the installed driver API. CI installs the
manifest requirements from PyPI. The shared-library release must be published
before that installation can succeed.
